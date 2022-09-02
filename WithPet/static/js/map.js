window.initMap = function () {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 33.4049875, lng: 126.4072028 },
    zoom: 14,
  });

  const malls = [
    { label: "C", name: "블리스풀", lat: 33.4049875, lng: 126.4072028 },
    { label: "G", name: "다같이애견카페", lat: 33.5202618, lng: 126.5658892 },
    { label: "D", name: "동대문시장", lat: 37.566596, lng: 127.007702 },
    { label: "I", name: "IFC몰", lat: 37.5251644, lng: 126.9255491 },
    { label: "L", name: "롯데월드타워몰", lat: 37.5125585, lng: 127.1025353 },
    { label: "M", name: "명동지하상가", lat: 37.563692, lng: 126.9822107 },
    { label: "T", name: "타임스퀘어", lat: 37.5173108, lng: 126.9033793 },
  ];

  malls.forEach(({ label, name, lat, lng }) => {
    const marker = new google.maps.Marker({
      position: { lat, lng },
      label,
      map: map,
    });
  });
};
