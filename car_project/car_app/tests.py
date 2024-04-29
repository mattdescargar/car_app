from faker import Faker
import random
from django.test import TestCase
from .models import Car

fake = Faker()


class GenerateCarsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Populate the database with 100,000 cars with random names
        cls.cars = [Car.objects.create(name=fake.word(), position=i) for i in range(1, 100001)]

        # Print the generated list with car names
        print("Initial Position -", end=" ")
        for car in cls.cars:
            print(f"Car {car.id}: {car.position}", end=", ")
        print()

    def test_switch_positions(self):
        # Select 10 pairs of random cars to switch positions
        pairs_to_switch = random.sample(range(1, 100001), 20)
        pairs_to_switch = [pairs_to_switch[i:i+2] for i in range(0, len(pairs_to_switch), 2)]

        for pair in pairs_to_switch:
            car1_id, car2_id = pair
            car1 = Car.objects.get(id=car1_id)
            car2 = Car.objects.get(id=car2_id)

            # Print the initial positions
            print(f"Initial Position - Car {car1.id}: {car1.position}, Car {car2.id}: {car2.position}")

            # Swap positions
            car1_position, car2_position = car1.position, car2.position
            car1.position, car2.position = car2_position, car1_position
            car1.save()
            car2.save()

            # Refresh the cars from the database
            car1.refresh_from_db()
            car2.refresh_from_db()

            # Print the final positions
            print(f"Final Position - Car {car1.id}: {car1.position}, Car {car2.id}: {car2.position}")

            # Check if the positions are updated correctly
            self.assertEqual(car1.position, car2_position)
            self.assertEqual(car2.position, car1_position)

        # Check if the positions of the remaining cars are not affected
        for car in Car.objects.exclude(id__in=[pair[0] for pair in pairs_to_switch]):
            original_position = car.position
            car.refresh_from_db()
            self.assertEqual(car.position, original_position)
