$( document ).ready(function() {

  const products = {{ products|safe }};
  let $body = $('#body');


  function renderBody(){
    $body.html('');
    products.forEach(product => {
      console.log(product);
      $body.append(`
            <article class="col-3 myProduct">
              <a class="myProductName" href="/product/${product.id}"><h3>${product.name}</h3></a>
              <p>${product.description}</p>
              <p>${product.units_sold} Units Sold</p>
              <div class="row">
                <small class="col-sm mr-auto MyBrand">${product.brand}</small>
                <small class="ml-auto mr-auto col-sm MyPrice">${product.price}$</small>
              </div>
            </article>`
      );
    });
    };

  renderBody();


  function comparePrice(a,b) {
    return a.price - b.price;
  };
  $('#SortByPrice').on('click', function() {
    products.sort(comparePrice);
    console.log(products);
    renderBody();
  });


  function compareName(a,b) {
    if(a.name < b.name) {return -1;}
    if(a.name > b.name) {return 1;}
    return 0;
  };
  $('#SortByProductName').on('click', function(){
    products.sort(compareName);
    console.log(products);
    renderBody();
  });


  function compareBestSelling(a,b) {
    if(a.units_sold > b.units_sold) {return -1;}
    if(a.units_sold < b.units_sold) {return 1;}
    return 0;
  };
  $('#SortByBestSelling').on('click', function(){
    products.sort(compareBestSelling);
    console.log(products);
    renderBody();
  });


  function compareBrandName(a,b) {
    if(a.brand < b.brand) {return -1;}
    if(a.brand > b.brand) {return 1;}
    return 0;
  };
  $('#SortByBrandName').on('click', function(){
    products.sort(compareBrandName);
    console.log(products);
    renderBody();
  });
});
