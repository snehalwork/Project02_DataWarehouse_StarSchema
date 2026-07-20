from sqlalchemy import text
from datetime import date


class SCDLoader:

    def update_customer_city(self,engine,customer_id,new_city,):

        with engine.begin() as connection:

            existing = connection.execute(
                text("""
                    SELECT customer_key, city
                    FROM dim_customer
                    WHERE customer_id=:customer_id
                    AND is_current='Y'
                """),
                {"customer_id": customer_id},
            ).fetchone()

            if existing is None:
                print("Customer not found.")
                return

            if existing.city == new_city:
                print("No Change.")
                return

            connection.execute(
                text("""
                    UPDATE dim_customer
                    SET
                        end_date=:today,
                        is_current='N'
                    WHERE customer_key=:customer_key
                """),
                {
                    "today": date.today(),
                    "customer_key": existing.customer_key,
                },
            )

            connection.execute(
                text("""
                    INSERT INTO dim_customer
                    (
                        customer_id,
                        first_name,
                        last_name,
                        gender,
                        city,
                        email,
                        created_date,
                        start_date,
                        end_date,
                        is_current
                    )

                    SELECT
                        customer_id,
                        first_name,
                        last_name,
                        gender,
                        :new_city,
                        email,
                        created_date,
                        :today,
                        NULL,
                        'Y'

                    FROM dim_customer

                    WHERE customer_key=:customer_key
                """),
                {
                    "today": date.today(),
                    "new_city": new_city,
                    "customer_key": existing.customer_key,
                },
            )

            print("SCD Type 2 Applied Successfully.")