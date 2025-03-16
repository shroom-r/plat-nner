/**
 * Add click listeners on attendee name to show toggle action buttons visibility
 */

import { initializeElementsVisibility } from "./initializeElementsVisibility.js";

document.querySelectorAll(".attendee-name").forEach((el) => {
  el.addEventListener("click", (event) => {
    var target = event.currentTarget;
    var targetIsSelected = target.classList.contains("selected");
    initializeElementsVisibility()
    if (!targetIsSelected) {
      target.classList.add("selected");
      target.parentNode
        .querySelector(".attendee-functions-container")
        .classList.remove("hidden");
    }
  });
});
