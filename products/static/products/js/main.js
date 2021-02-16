$(document).ready(async function () {
  $("#product_list").DataTable({
    serverSide: true,
    ajax: "/data/?format=datatables",
    columnDefs: [
      {
        targets: 1,
        data: "created_at",
        render: function (data, type, full, meta) {
          return new Date(data).toISOString().slice(0, 10);
        },
      },
    ],
  });
});
