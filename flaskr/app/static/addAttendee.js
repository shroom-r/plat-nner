/**
 * Add submit event listener to all add attendee forms
 * Add attendee with POST method on submit
 */
document.querySelectorAll(".addAttendeeForm").forEach((form) =>
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    var form = event.currentTarget;
    var formData = new FormData(form);
    var url = form.action;
    fetch(url, {
      method: "POST",
      body: formData,
    }).then((response) => {
      if (response.status == 200) {
        location.reload();
      }
      console.log(response);
    });
  })
);

/**
 * Add click events to show form button
 * Shows form on click
 */
document.querySelectorAll(".toggle-add-attendee-form-button").forEach((el) =>
  el.addEventListener("click", (event) => {
    var target = event.currentTarget;
    document
      .querySelectorAll(".toggle-add-attendee-form-button.hidden")
      .forEach((el) => el.classList.remove("hidden"));
    target.classList.add("hidden");
    var parent = target.closest("li");
    // Hide all forms
    document
      .querySelectorAll(".addAttendeeFormContainer:not(.hidden)")
      .forEach((el) => el.classList.add("hidden"));
    // Show wanted form
    var parentForm = parent
    .querySelector(".addAttendeeFormContainer")
    parentForm.classList.remove("hidden");
    parentForm.querySelector("input.attendee-name-input").focus()
  })
);
