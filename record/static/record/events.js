const URL = 'http://127.0.0.1:10000/api/events-list/'
const RequestAllEvents = new Request(URL, {
    method: "GET"
})

document.addEventListener('DOMContentLoaded', RequestEventsAPI(RequestAllEvents))

const GetAllEvents = document.querySelector('#all_events')
GetAllEvents.addEventListener('click', () => {
    RequestEventsAPI(RequestAllEvents)
});


const FilterForm = document.querySelector('#filter_form');
FilterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const RequestFilterEvents = new Request(URL, {
        method: "POST",
        body: new FormData(FilterForm)
    })
    RequestEventsAPI(RequestFilterEvents)
});


async function RequestEventsAPI(request) {
    let response = await fetch(request)
    let event_data = await response.json()
    CreateHTMLRecords(event_data)
}


function CreateHTMLRecords(event_data) {
    console.log(event_data)
    const div = document.querySelector('#records')
    const pagination = document.querySelector('#page')
    let records=''
    let pages = `
        <div class="pagination">
            <a href=${event_data.previous}>«</a>
            <a href=${event_data.next}>»</a>
        </div>`
    for (let elem of event_data.results) {
        let record = `
            <div class="row_main">
                <div id="recording">
                    <div id="description">
                        <p class="center"><a id="get_organization" href="url">${ elem.organization__name}</a></p>
                        <a id="event" href="url">${elem.name}</a>
                        <p> Дата: ${elem.date_event}</p>
                        <p> Время: с ${elem.start_time} по ${elem.end_time}</p>
                        <p> Лимит участников: ${elem.limit_clients} </p>
                        <p> Количество участников: ${elem.quantity_clients} </p>
                        <p> Цена: ${elem.price_event}</p>
                        <p class="center"><a id="get_recording" href="url">Записаться</a></p>
                    </div>
                </div>
            </div>
            `
        records += record
    }
    div.innerHTML = records
    pagination.innerHTML = pages

}

