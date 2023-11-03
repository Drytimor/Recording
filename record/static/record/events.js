async function getEvent() {
    let div = await document.getElementById('central')
    let url = 'http://127.0.0.1:10000/api/events'
    let response = await fetch(url)
    let data = await response.json()

    for(let elem of data){
        let record = `
            <div class="row_main">
                <div id="recording">
                    <div id="description">
                        <p class="organization"><a id="get_organization" href="url">${ elem.organization__name}</a></p>
                        <a id="event" href="url">${elem.name}</a>
                        <p> Дата: ${elem.date_event}</p>
                        <p> Время: с ${elem.start_time} по ${elem.end_time}</p>
                        <p> Лимит участников: ${elem.limit_clients} </p>
                        <p> Количество участников: ${elem.quantity_clients} </p>
                        <p> Цена: ${elem.price_event}</p>
                        <p class="organization"><a id="get_recording" href="url">Записаться</a></p>
                    </div>
                </div>
            </div>
            `

        div.innerHTML += record
    }
}