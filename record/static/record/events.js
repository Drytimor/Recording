
document.addEventListener('DOMContentLoaded', RequestEventsAPI('http://127.0.0.1:10000/api/events-list/'))

const Pagination = document.querySelector('#page')
Pagination.addEventListener('click', (e) => {
    e.preventDefault()
    let url = new URL(e.srcElement.href)
    if (url.search) {
        RequestEventsAPI(url)
    }
})

const RegistrationForm = document.querySelector('#registration_form')
RegistrationForm.addEventListener("submit", (e) => {
    const url = new URL('http://127.0.0.1:10000/api/registration/')
    e.preventDefault()
    const request = new Request(url, {
        method: "POST",
        body: new FormData(RegistrationForm),
    });
    const FormRegistr = new FormData(RegistrationForm)
    for (let [name, value] of FormRegistr.entries()) {
        console.log(name, value)
    }
    console.log(request)
    CreateUserApi(request)
})

async function CreateUserApi(request){
    let response = await fetch(request)
    let event_data = await response.json()
    console.log(event_data)
}

const FilterForm = document.querySelector('#filter_form');

FilterForm.addEventListener('submit',  ListenerForm)
FilterForm.addEventListener('reset', ListenerForm)


function ListenerForm(e) {
    const url = new URL('http://127.0.0.1:10000/api/events-list/')
    e.preventDefault();
    if (e.type === "submit") {
        let paramFilter = new URLSearchParams()
        const form = new FormData(FilterForm)
        for (let [name, value] of form.entries()) {
            paramFilter.append(name, value)
            }
        url.search = paramFilter
    } else {
        url.search = ''
        for (f of FilterForm) {
            f.checked = false
            }
    }
    RequestEventsAPI(url)
}


async function RequestEventsAPI(request) {
    let response = await fetch(request)
    let event_data = await response.json()
    CreateHTMLEvents(event_data)
}


function CreateHTMLEvents(event_data) {
    CreateRecordingsHTML(event_data.results, event_data.count)
    CreatePaginationHTML(event_data.page_links, event_data.previous, event_data.next, event_data.count)
}


function CreateRecordingsHTML (results, records_count) {
    const records = document.querySelector('#records')
    if (records_count == 0) {
        DisplaysMessageForEmptySearch(records)
    } else {
        let records_html=''
        for (let elem of results) {
            if (elem.price_event == null) {
                elem.price_event = 'бесплатно'
            } else {
                elem.price_event += ' р'
            }
            let record = `
            <div class="card text-dark bg-light mb-2">
                <div class="row g-0 ">
                    <div class="col-md-4">
                        <img src="" class="img-fluid rounded-start" alt="">
                    </div>
                    <div class="col-md-8 g-0">
                        <div class="card-body">
                        <h5 class="text-center card-title"><a class="text-decoration-none" href="">${ elem.organization__name}</a></h5>
                        <ul>
                            <li class="d-block"><a class="text-decoration-none" href="">${elem.name}</a></li>
                            <li class="d-block"> Дата: ${elem.date_event}</li>
                            <li class="d-block"> Время: с ${elem.start_time} по ${elem.end_time}</li>
                            <li class="d-block"> Лимит участников: ${elem.limit_clients} </li>
                            <li class="d-block"> Количество участников: ${elem.quantity_clients} </li>
                            <li class="d-block"> Цена: ${elem.price_event}</li>
                        </ul>
                        <p class="text-center mb-0"><a class="text-decoration-none btn-sm btn-dark" href="">Записаться</a></p>
                        </div>
                    </div>
                </div>
            </div>
            `
            records_html +=record
        }
        records.innerHTML = records_html
    }
}


function CreatePaginationHTML (page_links, page_previous, page_next, count_page) {
    const pagination = document.querySelector('#page')
    const urlPage = new URL('http://127.0.0.1:10000/api/events-list/')
    if (count_page == 0) {
        pagination.firstElementChild.remove()
    } else {
        const paramPage = new URLSearchParams()
        const default_limit_page = 2
        let offset_param_page = 0
        paramPage.append('limit', default_limit_page)
        paramPage.append('offset', offset_param_page)
        urlPage.search = paramPage
        let page_number_html = ''
        for (let [page_url, number_page, active_link] of page_links) {
            urlPage.searchParams.set('offset', offset_param_page)
            offset_param_page += 2
            let css_active = ''
            if(active_link) {
                css_active += 'active'}
            page_number_html += `
                <li class="page-item ${css_active}">
                    <a class="page-link" href="${urlPage.href}">${number_page}</a>
                </li>
                `
            }
        let pagination_html = `
            <ul class="pagination pagination-sm justify-content-center">
                <li class="page-item">
                    <a class="page-link" href=${page_previous}>«</a>
                </li>
                ${page_number_html}
                <li class="page-item">
                    <a class="page-link" href=${page_next}>»</a>
                </li>
            </ul>
            `
        pagination.innerHTML = pagination_html
    }
}


function DisplaysMessageForEmptySearch (records) {
    let message = `
        <h1 class="text-center fst-italic text-secondary">
            пусто
        </h1>
        `
    records.innerHTML = message
}