window.onload = function() {
  var request = new XMLHttpRequest();
  request.open("GET", URL_SALES);
  request.onload = function() {
    if (request.status == 200) {
      updateSales(request.responseText);
    }
  }
  request.send(null);
}

function updateSales(responseText) {
  var salesDiv = document.getElementById("sales");
  salesDiv.innerHTML = responseText;
}
