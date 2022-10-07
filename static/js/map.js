function initMap() {
    const uluru = { lat: 49.9967710077131, lng: 36.2334176050233 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 18.92,
        center: uluru,
    });
    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
    })
}

window.initMap = initMap;