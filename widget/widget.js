(async function () {
  const iframe = document.createElement("iframe");
  iframe.src = "https://YOUR_DOMAIN/iframe.html";
  iframe.style.position = "fixed";
  iframe.style.bottom = "20px";
  iframe.style.right = "20px";
  iframe.style.width = "350px";
  iframe.style.height = "500px";
  iframe.style.border = "none";
  iframe.style.zIndex = "9999";
  document.body.appendChild(iframe);
})();
