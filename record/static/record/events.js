const url = new URL('http://127.0.0.1:10000/api/events-list/')


const RequestAllEvents = new Request(url.origin + url.pathname, {
    method: "GET"
})

document.addEventListener('DOMContentLoaded', RequestEventsAPI(RequestAllEvents))

const GetAllEvents = document.querySelector('#all_events')
GetAllEvents.addEventListener('click', () => {
    for (f of FilterForm) {
        f.checked = false
}
    RequestEventsAPI(RequestAllEvents)
});


const Pagination = document.querySelector('#page')
Pagination.addEventListener('click', (e) => {
    e.preventDefault()
    let url = new URL(e.srcElement.href)
    if (url.search) {
        RequestEventsAPI(url)
    }
})


const FilterForm = document.querySelector('#filter_form');

FilterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let paramFilter = new URLSearchParams()
    const form = new FormData(FilterForm)
    for (let [name, value] of form.entries()) {
        paramFilter.append(name, value)
    }
    url.search = paramFilter
    RequestEventsAPI(url)
});


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
                <div class="recording">
                <div id="description">
                    <p class="center"><a id="organization_name" href="url">${ elem.organization__name}</a></p>
                    <ul>
                        <li><a id="event_name" href="url">${elem.name}</a></li>
                        <li> Дата: ${elem.date_event}</li>
                        <li> Время: с ${elem.start_time} по ${elem.end_time}</li>
                        <li> Лимит участников: ${elem.limit_clients} </li>
                        <li> Количество участников: ${elem.quantity_clients} </li>
                        <li> Цена: ${elem.price_event}</li>
                    </ul>
                    <p class="center"><a id="sign_up" href="url">Записаться</a></p>
                </div>
                </div>
                `
            records_html += record
        }
        records.innerHTML = records_html
    }
}

function CreatePaginationHTML (page_links, page_previous, page_next, count_page) {
    const pagination = document.querySelector('#page')
    if (count_page == 0) {
        pagination.firstElementChild.remove()
    } else {
        let page_number_html = ``
        for (let [url_page, number_page, active_link] of page_links) {
            let css_active = ''
            if(active_link) {
                css_active += 'active'}
            page_number_html += `<a class="${css_active}" href="${url_page}">${number_page}</a>`
            }
        let pagination_html = `
            <div class="pagination">
                <a href=${page_previous}>«</a>
                ${page_number_html}
                <a href=${page_next}>»</a>
            </div>
            `
        pagination.innerHTML = pagination_html
    }

}

function DisplaysMessageForEmptySearch (records) {
    let message = `
        <div class="center" id="message_empty">
            пусто
        </div>
    `
    records.innerHTML = message
}