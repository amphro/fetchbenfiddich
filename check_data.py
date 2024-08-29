import requests
import sys

def check_availability():
    url = "https://production-booking.tablecheck.com/v2/booking/availability_v4/dates"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
    }
    data = {
      "shop_id": "benfiddich-tokyo",
      "start_at": "2024-09-19T19:00:00.000+09:00",
      "pax_adult": 2,
      "pax_senior": 0,
      "pax_child": 0,
      "pax_baby": 0,
      "service_category_ids": [
        "661e2ceaeefe0c01f9b2c054","661e2cf31ec3ef01ef82a0b9"
      ],
      "manual_duration": nil,
      "start_date": "2024-09-20T19:00:00.000+09:00",
      "end_date": "2024-09-27T23:59:59.000+09:00",
      "orders": [],
      "use_experience_page": false,
      "locale": "en"
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        print("Data found in response:")
        print(response_data)
        availability_dates = response_data.get("availability_dates")
        if availability_dates.get("data"):
            # Exit with status 1 if data is not empty
            sys.exit(1)
        else:
            # Exit with status 0 if data is empty
            sys.exit(0)
    else:
        # Exit with status 2 if the request failed
        print(response.text)
        sys.exit(2)

if __name__ == "__main__":
    check_availability()
