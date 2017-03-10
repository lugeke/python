function getNsrsbh() {
  var doc = document.getElementById('iframe').contentWindow.document;
  var nsrInfo = doc.getElementsByTagName("table")[0].rows[0].cells[0].innerHTML;
  var nsr = nsrInfo.match(/[A-Za-z0-9]+/);
  
  //alert(nsr);
  var body = document.body;
  var input = document.createElement("input");
  input.id = "result_nsr_ds";
  input.value = nsr;
  input.type = "hidden"
  body.appendChild(input);
}
getNsrsbh()