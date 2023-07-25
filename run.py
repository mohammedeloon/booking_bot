from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.select_place_to_go('Madrid')
    # bot.select_dates(check_in_date="2023-08-08",
    #                  check_out_date="2023-09-08")
    # bot.select_adults(3)
    bot.click_search()
    bot.refresh()
    bot.report_results()
