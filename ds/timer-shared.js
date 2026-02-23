(function () {
  const elements = get_elements();

  const d = elements["d"],
    go = elements["go"],
    pa = elements["pa"],
    mIn = elements["mIn"],
    sIn = elements["sIn"];

  let iv = null,
    left = 0,
    running = false,
    paused = false;

  function fmt(s) {
    return (
      String(Math.floor(s / 60)).padStart(2, "0") +
      ":" +
      String(s % 60).padStart(2, "0")
    );
  }

  function stop() {
    clearInterval(iv);
    iv = null;
    running = false;
    paused = false;
    go.textContent = "GO";
    pa.style.display = "none";
  }

  function tick() {
    if (left <= 0) {
      stop();
      d.style.color = "#f44";
      d.textContent = "00:00";
      return;
    }
    left--;
    d.textContent = fmt(left);
    if (left <= 10) d.style.color = "#f44";
  }

  go.onclick = function () {
    if (running) {
      stop();
      return;
    }
    left = (parseInt(mIn.value) || 0) * 60 + (parseInt(sIn.value) || 0);
    if (left <= 0) return;
    d.style.color = "#0f0";
    d.textContent = fmt(left);
    running = true;
    paused = false;
    go.textContent = "\u25A0";
    pa.style.display = "inline-block";
    iv = setInterval(tick, 1000);
  };

  pa.onclick = function () {
    if (paused) {
      paused = false;
      pa.innerHTML = "&#9678;";
      pa.style.background = "#fa0";
      iv = setInterval(tick, 1000);
    } else {
      paused = true;
      pa.textContent = "\u25B6";
      pa.style.background = "#0af";
      clearInterval(iv);
      iv = null;
    }
  };
})();
