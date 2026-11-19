(function () {
  var btn = document.querySelector(".menu-btn");
  var list = document.getElementById("nav-list");
  if (btn && list) {
    btn.addEventListener("click", function () {
      var open = list.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
  }

  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  var tablist = document.querySelector('[role="tablist"]');
  if (tablist) {
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]'));
    var select = function (tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
      });
    };
    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab); });
      tab.addEventListener("keydown", function (e) {
        var next = null;
        if (e.key === "ArrowRight" || e.key === "ArrowDown") next = tabs[(i + 1) % tabs.length];
        if (e.key === "ArrowLeft" || e.key === "ArrowUp") next = tabs[(i - 1 + tabs.length) % tabs.length];
        if (e.key === "Home") next = tabs[0];
        if (e.key === "End") next = tabs[tabs.length - 1];
        if (next) { e.preventDefault(); select(next); next.focus(); }
      });
    });
  }

  var slider = document.querySelector(".slider");
  if (slider) {
    document.querySelectorAll(".slide-btn").forEach(function (b) {
      b.addEventListener("click", function () {
        var card = slider.querySelector(".post-card");
        var step = card ? card.getBoundingClientRect().width + 24 : 320;
        slider.scrollBy({ left: step * Number(b.dataset.dir), behavior: "smooth" });
      });
    });
  }

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window && !reduce) {
    var format = function (el, v) {
      var target = el.dataset.count;
      var decimals = target.indexOf(".") > -1 ? target.split(".")[1].length : 0;
      var n = decimals ? v.toFixed(decimals) : Math.round(v).toLocaleString("en-SG");
      el.textContent = (el.dataset.prefix || "") + n + (el.dataset.suffix || "");
    };
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        var el = entry.target, end = parseFloat(el.dataset.count), start = performance.now();
        var tick = function (now) {
          var t = Math.min(1, (now - start) / 1200);
          format(el, end * (1 - Math.pow(1 - t, 3)));
          if (t < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { io.observe(el); });
  }

  var form = document.getElementById("contact-form");
  if (!form) return;
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var ok = true;
    form.querySelectorAll("[required]").forEach(function (field) {
      var err = field.parentElement.querySelector(".err");
      var empty = !field.value.trim();
      var badEmail = field.type === "email" && !/^\S+@\S+\.\S+$/.test(field.value.trim());
      var bad = empty || badEmail;
      err.textContent = bad ? (badEmail && !empty ? "Enter an email address." : "This field is required.") : "";
      field.setAttribute("aria-invalid", bad ? "true" : "false");
      if (bad) ok = false;
    });
    if (!ok) return;
    var value = function (id) {
      var el = document.getElementById(id);
      return el ? el.value.trim() : "";
    };
    var subject = "WorkNest SG: " + (value("topic") || "message");
    var body = "Name: " + value("name") + "\nEmail: " + value("email") + "\n\n" + value("msg");
    form.hidden = true;
    var done = document.getElementById("form-ok");
    done.hidden = false;
    done.focus();
    window.location.href = "mailto:support@worknestsg.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
  });
})();
