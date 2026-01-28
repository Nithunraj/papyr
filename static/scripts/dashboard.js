function openTransactionPopup(transactionId, title, walletId, categoryId, title) {
    console.log(transactionId,title,walletId);

    document.getElementById("transactionModal").classList.add("active");

    const titleInput = document.getElementById("title");
    titleInput.value = title;
    titleInput.readOnly = true;

    const walletSelect = document.getElementById("wallet");
    walletSelect.value = walletId;

    const categorySelect = document.getElementById("category");
    categorySelect.value = categoryId;

    walletSelect.disabled = true;
    categorySelect.disabled = true;
}

const ModalEditTransactions = {
  open() {
    document.getElementById("transactionModal").classList.add("active");
  },
  close() {
    document.getElementById("transactionModal").classList.remove("active");
    Form.clearFields();
  },
};