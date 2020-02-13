from selenium.webdriver.support.ui import Select


def website_text(selenium):
    return selenium.find_element_by_tag_name("body").text


def test_rent_single_car(selenium):
    selenium.get("http://qalab.pl.tivixlabs.com/")
    assert "Car rent" in selenium.title

    search_form_elements = selenium.find_elements_by_css_selector("#search_form")
    assert len(search_form_elements) > 0

    select_country = Select(selenium.find_element_by_name("country"))
    select_country.select_by_visible_text("Poland")

    select_city = Select(selenium.find_element_by_name("city"))
    select_city.select_by_visible_text("Wroclaw")

    model_input = selenium.find_element_by_name("model")
    model_input.clear()
    model_input.send_keys("Toyota RAV4")

    pickup_input = selenium.find_element_by_name("pickup")
    pickup_input.send_keys("02132020")

    dropoff_input = selenium.find_element_by_name("dropoff")
    dropoff_input.send_keys("02172020")

    search_button = selenium.find_element_by_xpath("//*[@id='search_form']/button")
    search_button.click()

    company_name_element = selenium.find_element_by_xpath(
        "//*[@id='search-results']/tbody/tr[1]/td[1]"
    )
    model_name_element = selenium.find_element_by_xpath(
        "//*[@id='search-results']/tbody/tr[1]/td[2]"
    )
    license_plate_element = selenium.find_element_by_xpath(
        "//*[@id='search-results']/tbody/tr[1]/td[3]"
    )
    price_element = selenium.find_element_by_xpath(
        "//*[@id='search-results']/tbody/tr[1]/td[4]"
    )
    price_per_day_element = selenium.find_element_by_xpath(
        "//*[@id='search-results']/tbody/tr[1]/td[5]"
    )
    assert company_name_element.text == "Charles-Alvarez"
    assert model_name_element.text == "Toyota RAV4"
    assert license_plate_element.text == "9W3J3KBI"
    assert price_element.text == "$255"
    assert price_per_day_element.text == "$51"

    rent_button = selenium.find_element_by_xpath(
        "//*[@id='search-results']/tbody/tr[1]/td[6]/a"
    )
    rent_button.click()

    header_element = selenium.find_element_by_class_name("card-header")
    assert header_element.text == "Toyota RAV4"

    text_from_website = website_text(selenium)
    assert "Company: Charles-Alvarez" in text_from_website
    assert "Price per day: $51" in text_from_website
    assert "Location: Poland, Wroclaw" in text_from_website
    assert "License plate: 9W3J3KBI" in text_from_website
    assert "Pickup date: 2020-02-13" in text_from_website
    assert "Dropoff date: 2020-02-17" in text_from_website

    rent_confirm_button = selenium.find_element_by_xpath(
        "//*[contains(text(),'Rent!')]"
    )
    rent_confirm_button.click()

    assert "Summary:" in website_text(selenium)

    name_input = selenium.find_element_by_name("name")
    name_input.send_keys("John")
    last_name_input = selenium.find_element_by_name("last_name")
    last_name_input.send_keys("Doe")
    card_number_input = selenium.find_element_by_name("card_number")
    card_number_input.send_keys("4024007191948792")
    email_input_element = selenium.find_element_by_name("email")
    email_input_element.send_keys("john.doe@example.com")
    rent_final_button = selenium.find_element_by_xpath("//*[contains(text(),'Rent')]")
    rent_final_button.click()

    assert "Success" in website_text(selenium)
