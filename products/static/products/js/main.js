$(document).ready(async function () {
  try {
    async function getData() {
      const response = await fetch("http://127.0.0.1:8000/data/");
      const jsonData = await response.json();

      return jsonData;
    }

    function prepareDataSet(jsonData) {
      return jsonData.map((product) => Object.values(product));
    }

    function prepareColumns(jsonData) {
      const raw_columns = Object.keys(jsonData[0]);

      const formatted_columns = raw_columns.map((column) => {
        let title = "";
        let render = undefined;

        switch (column) {
          case "product_url":
            title = "Produto";
            render = (data, type, row) =>
              `<a href="${data}" target="_blank" rel="nofollow">${data}</a>`;
            break;
          case "created_at":
            title = "Data de inserção na loja";
            render = (data, type, row) =>
              new Date(data).toISOString().slice(0, 10);
            break;
          case "sales":
            title = "Total de vendas";
            break;
          default:
            title = new Date(column).toLocaleDateString("pt-br", {
              dateStyle: "long",
              timeZone: "UTC",
            });
            break;
        }

        return { title, render };
      });

      return formatted_columns;
    }

    const jsonData = await getData();

    const data = prepareDataSet(jsonData);
    const columns = prepareColumns(jsonData);

    const dataTableOptions = {
      data,
      columns,
    };

    $("#product_list").DataTable(dataTableOptions);
  } catch {
    alert("Não foi possível recuperar os dados da API...");
  }
});
