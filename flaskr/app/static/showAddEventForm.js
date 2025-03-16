/**
 * Add event listener to show-add-event-form-button button
 * On click, show form
 */

import { initializeElementsVisibility } from "./initializeElementsVisibility.js";

document
  .querySelector("#show-add-event-form-button")
  .addEventListener("click", (event) => {
    var target = event.currentTarget;
    // Initialize form and buttons visibility and show add event form
    initializeElementsVisibility();
    var form = document.querySelector("#new-event-card");
    form.classList.remove("hidden");
    form.scrollIntoView({ behavior: "smooth" });
    form.querySelector("input#date").focus()
  });
