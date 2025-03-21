/**
 * Add click listeners on button to toggle post functions visibility
 */

import { initializeElementsVisibility } from "./initializeElementsVisibility.js";

document.querySelectorAll(".toggle-post-functions-button").forEach((el) => {
  el.addEventListener("click", (event) => {
    var target = event.currentTarget.closest(".post-container");
    var targetIsSelected = target.classList.contains("selected");
    initializeElementsVisibility()
    if (!targetIsSelected) {
      target.classList.add("selected");
      target
        .querySelector(".post-functions-container")
        .classList.remove("hidden");
    }
  });
});
