/**
 * Add click listeners on button to toggle event functions visibility
 */

import { initializeElementsVisibility } from "./initializeElementsVisibility.js";

document.querySelectorAll(".toggle-event-functions-button").forEach((el) => {
  el.addEventListener("click", (event) => {
    var target = event.currentTarget.closest(".event-card");
    var targetIsSelected = target.classList.contains("selected");
    initializeElementsVisibility();
    if (!targetIsSelected) {
      target.classList.add("selected");
      target
        .querySelector(".event-functions-container")
        .classList.remove("hidden");
    }
  });
});
