

$(function () {

    $(".favorite-removed").on("click", function (evt) {
        var trip_id = $(this).data('tripid');
        var favorite = $(this).data('favorite');
        $(this).toggleClass("favorite");

        var data = {'trip_id': trip_id, 'favorite': favorite};
        $.post("/add-to-favorites.json", data, addToFavoritesSuccess);

    });

  });


function addToFavoritesSuccess(result) {
              
        console.log("You have added this to your bucket list!");


      }



