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
