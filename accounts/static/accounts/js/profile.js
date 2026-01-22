const editBtn = document.getElementById("editProfileBtn");
const modal = document.getElementById("editProfileModal");
const closeBtn = document.getElementById("close-modal-btn");
const profileCancelButton = document.getElementById("closeModal");

editBtn.addEventListener("click", function (e) {
  e.preventDefault();
  modal.classList.add("active");
});

closeBtn.addEventListener("click", function () {
  modal.classList.remove("active");
});

profileCancelButton.addEventListener("click", function () {
  modal.classList.remove("active");
});

// Close when clicking outside modal
modal.addEventListener("click", function (e) {
  if (e.target === modal) {
    modal.classList.remove("active");
  }
});

const passwordChangeBtn = document.getElementById("changePasswword");
const changePasswordModal = document.getElementById("changePasswordButton");

passwordChangeBtn.addEventListener("click", function (e) {
  e.preventDefault();
  changePasswordModal.classList.add("active");
});