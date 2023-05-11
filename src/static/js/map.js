ymaps.ready(init);

function init() {

    var initLat;
    initLat = document.getElementById('id_latitude').value;
    var initLong;
    initLong = document.getElementById('id_longitude').value;

    if (!initLat || !initLong) {
        initLat = 56.83796762499889,
        initLong = 60.60386618144089;
        document.getElementById('id_latitude').value = initLat;
        document.getElementById('id_longitude').value = initLong;
    };

    var myPlacemark,
        myMap = new ymaps.Map('map', {
            center: [initLat, initLong],
            zoom: 13,
            controls: ['zoomControl']
        }, {
            searchControlProvider: 'yandex#search'
        });

    myPlacemark = createPlacemark([initLat, initLong],);
    myMap.geoObjects.add(myPlacemark);

    // Слушаем клик на карте.
    myMap.events.add('click', function (e) {
        var coords = e.get('coords');

        // Если метка уже создана – просто передвигаем ее.
        if (myPlacemark) {
            myPlacemark.geometry.setCoordinates(coords);
        }
        // Если нет – создаем.
        else {
            myPlacemark = createPlacemark(coords);
            myMap.geoObjects.add(myPlacemark);
        }

        document.getElementById('id_latitude').value = coords[0];
        document.getElementById('id_longitude').value = coords[1];
    });

    // Создание метки.
    function createPlacemark(coords) {
        return new ymaps.Placemark(coords, {
            iconCaption: ''
        }, {
            preset: 'islands#violetDotIconWithCaption',
            draggable: false
        });
    }
}
