from selenium.webdriver.common.by import By
import booking.constants as const
from selenium import webdriver
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9222")
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.XPATH, '//*[@id=":Ra9:"]')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.XPATH,
                                         '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[1]/div/div/div[2]/ul/li[1]'
                                         )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.XPATH,
                                             '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/span'
                                             )
        check_in_element.click()

        check_out_element = self.find_element(By.XPATH,
                                              '//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[3]/td[5]/span'
                                              )
        check_out_element.click()

    def click_search(self):
        search_button = self.find_element(By.XPATH,
                                          '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[4]/button'
                                          )
        search_button.click()

    def report_results(self):
        hotel_boxes = self.find_element(By.XPATH,
                                        '//*[@id="search_results_table"]/div[2]/div/div/div[3]'
                                        )

        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
