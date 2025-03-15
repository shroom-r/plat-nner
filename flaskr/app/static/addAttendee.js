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
    var parentForm = parent.querySelector(".addAttendeeFormContainer");
    parentForm.classList.remove("hidden");
    parentForm.querySelector("input.attendee-name-input").focus();
  })
);
