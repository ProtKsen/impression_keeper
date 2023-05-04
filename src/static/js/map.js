ymaps.ready(init);

function init() {

    var initLat;
    initLat = document.getElementById('id_latitude').value;
    var initLong;
    initLong = document.getElementById('id_longitude').value;

    if (!initLat || !initLong) {
        initLat = 56.85194,
        initLong = 60.6122;
        document.getElementById('id_latitude').value = initLat;
        document.getElementById('id_longitude').value = initLong;
    };

    var myPlacemark,
        myMap = new ymaps.Map('map', {
            center: [initLat, initLong],
            zoom: 9
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
            // Слушаем событие окончания перетаскивания на метке.
            myPlacemark.events.add('dragend', function () {
                getAddress(myPlacemark.geometry.getCoordinates());
            });
        }
        getAddress(coords);

        document.getElementById('id_latitude').value = coords[0];
        document.getElementById('id_longitude').value = coords[1];
    });

    // Создание метки.
    function createPlacemark(coords) {
        return new ymaps.Placemark(coords, {
            iconCaption: ''
        }, {
            preset: 'islands#violetDotIconWithCaption',
            draggable: true
        });
    }

    // Определяем адрес по координатам (обратное геокодирование).
    function getAddress(coords) {
        myPlacemark.properties.set('iconCaption', 'поиск...');
        ymaps.geocode(coords).then(function (res) {
            var firstGeoObject = res.geoObjects.get(0);

            myPlacemark.properties
                .set({
                    // Формируем строку с данными об объекте.
                    iconCaption: [
                        // Название населенного пункта или вышестоящее административно-территориальное образование.
                        firstGeoObject.getLocalities().length ? firstGeoObject.getLocalities() : firstGeoObject.getAdministrativeAreas(),
                        // Получаем путь до топонима, если метод вернул null, запрашиваем наименование здания.
                        firstGeoObject.getThoroughfare() || firstGeoObject.getPremise()
                    ].filter(Boolean).join(', '),
                    // В качестве контента балуна задаем строку с адресом объекта.
                    balloonContent: firstGeoObject.getAddressLine()
                });
        });
    }
}
