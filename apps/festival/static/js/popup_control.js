function getCookie(name) {
  var nameOfCookie = name + "=";
  var x = 0;
  while (x <= document.cookie.length) {
    var y = x + nameOfCookie.length;
    if (document.cookie.substring(x, y) == nameOfCookie) {
      if ((endOfCookie = document.cookie.indexOf(";", y)) == -1) endOfCookie = document.cookie.length;
      return unescape(document.cookie.substring(y, endOfCookie));
    }

    x = document.cookie.indexOf(" ", x) + 1;

    if (x == 0) break;
  }
  return "";
}

function setCookie(name, value, expiredays) {
  var todayDate = new Date();
  todayDate.setDate(todayDate.getDate() + expiredays);
  document.cookie = name + "=" + escape(value) + "; path=/; expires=" + todayDate.toGMTString() + ";";
}

function closeWin(get_Key) {
  get_Pop = eval("document.all.Popup" + get_Key);
  get_Pop_id = "Popup" + get_Key;

  if (get_Pop.checked) {
    setCookie(get_Pop_id, "done", 1);
  }

  get_layerPopup = eval("document.all.layerPopup" + get_Key);
  get_layerPopup.style.display = "none";
}

var x = 0;
var y = 0;
drag = 0;
move = 0;
window.document.onmousemove = mouseMove;
window.document.onmousedown = mouseDown;
window.document.onmouseup = mouseUp;
window.document.ondragstart = mouseStop;

function mouseUp() {
  move = 0;
}
function mouseDown() {
  if (drag) {
    //alert(parseInt(dragObj.style.left));
    clickleft = window.event.clientX - parseInt(dragObj.style.left);
    clicktop = window.event.clientY - parseInt(dragObj.style.top);
    dragObj.style.zIndex += 1;
    move = 1;
  }
}
function mouseMove() {
  if (move) {
    dragObj.style.left = window.event.x - clickleft;
    dragObj.style.top = window.event.y - clicktop;
  }
}
function mouseStop() {
  window.event.returnValue = false;
}
function Show(divid) {
  divid.filters.blendTrans.apply();
  divid.style.visibility = "visible";
  divid.filters.blendTrans.play();
}
function Hide(divid) {
  divid.filters.blendTrans.apply();
  divid.style.visibility = "hidden";
  divid.filters.blendTrans.play();
}

/* Popup 1 */
if (getCookie("Popup0") != "done") {
  document.all.layerPopup0.style.display = "block";
}

/* Popup 2 */
if (getCookie("Popup1") != "done") {
  document.all.layerPopup1.style.display = "block";
}

layerPopup0 = document.getElementById("layerPopup0");
layerPopup0.style.top = 70;
layerPopup0.style.left = 70;

layerPopup1 = document.getElementById("layerPopup1");
layerPopup1.style.top = 500;
layerPopup1.style.left = 70;
