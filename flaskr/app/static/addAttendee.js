/**
 * Add click events to show form button
 * Shows form on click
 */

import { initializeElementsVisibility } from "./initializeElementsVisibility.js";

document.querySelectorAll(".toggle-add-attendee-form-button").forEach((el) =>
  el.addEventListener("click", (event) => {

    initializeElementsVisibility()

    var target = event.currentTarget;
    // Hide current toggle button
    target.classList.add("hidden");
    var parent = target.closest("li");
    // Show wanted form
    var parentForm = parent.querySelector(".addAttendeeFormContainer");
    parentForm.classList.remove("hidden");
    parentForm.querySelector("input.attendee-name-input").focus();
  })
);
