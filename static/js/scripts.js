$(document).ready(function() {

    // function redirect_on_book(){

    //     window.location.href = "https://www.kayak.com/flights/origin-destination/start-date/return-date"
    // }

    // $("#book").


//     function submitUserCriteria (evt) {
//         // add later, remove hardcoded data
//         // var formInput = {
//         //     "origin": $("#origin").val(),
//         //     "budget": $("#budget").val(),
//         //     "start-date": $("#start-date").val(),
//         //     "return-date": $("#return-date").val()
//         // };

//         // remove below hardcoded data later
//         var formInput = {
//             "origin": "SFO",
//             "budget": "500",
//             "start-date": 08/21/2017,
//             "return-date": 08/25/2017
//         };
// <!-- <tr><td>
//                     <form action="/book/{{ dest }}" method="POST">
//                       <input type="hidden" name="origin" value="{{  item['origin']  }}">
//                       <input type="hidden" name="destination" value="{{  item['destination']  }}">
//                       <input type="hidden" name="start-date" value="{{  item['depature_time']  }}"> -->
//                       <!-- </form> -->

// }

// $("#user-criteria").on("submit", submitUserCriteria);


// # @app.route('/book/<dest>')
// # def book_flights(dest):
// #     """Redirects user to kayak's booking portal."""

//     # flight_results = session['flight_results']
//     # origin = flight_results[0][0]['origin']
//     # destination = flight_results[0][0]['destination']
//     # start_date = flight_results[0][0]['departure_time']
//     # return_date = flight_results[0][1]['departure_time']



// #     return redirect("https://www.kayak.com/flights/<origin>-<destination>/<start-date>/<return-date>")


<form action="/book" method="POST">
                        <input type="hidden" name="origin" value=" {{ item['origin'] }}">
                        <input type="hidden" name="destination" value="{{ item['destination'] }}">
                        <input type="hidden" name="start-date" value="{{ item['depature_time'] }}">

                        </form>




















































    });