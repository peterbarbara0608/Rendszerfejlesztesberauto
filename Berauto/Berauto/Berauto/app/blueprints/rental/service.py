class RentalService:
    _rentals = {}
    _id_counter = 1

    @classmethod
    def create_rental(cls, data):
        rental_id = cls._id_counter
        rental_data = {
            "rental_id": rental_id,
            "car_model": data["car_model"],
            "renter_name": data["renter_name"],
            "rental_date": str(data["rental_date"]),
            "return_date": str(data.get("return_date", "")),
            "price": data.get("price", 0)
        }
        cls._rentals[rental_id] = rental_data
        cls._id_counter += 1
        return True, rental_data

    @classmethod
    def get_rental(cls, rental_id):
        rental = cls._rentals.get(rental_id)
        if rental:
            return True, rental
        return False, "Rental not found."
