from src.common.dto import justJoinItDTO


class DTOParser:
    @staticmethod
    def parse(data: dict[str, str | bool | int | list[dict[str,str|float]]]) -> justJoinItDTO:
        return justJoinItDTO(
            slug = data.get("slug"),
            title = data.get("title"),
            company = data.get("companyName"),
            comapnyLogoUrl = data.get("companyLogoThumbUrl"),
            requiredSkills = data.get("requiredSkills"),
            remoteInterview = data.get("remoteInterview"),
            openToHireUkrainians = data.get("openToHireUkrainians"),
            salary = [
                justJoinItDTO.Salary(
                    employmentType = salary.get("type"),
                    salaryFrom = salary.get("from"),
                    salaryTo = salary.get("to")
                ) for salary in data.get("employmentTypes")
            ],
            workPlace = data.get("workplaceType"),
            publishedAt = data.get("publishedAt"),
            primaryLocation = justJoinItDTO.Location(
                city = data.get("city"),
                slug = data.get("slug"),
                street = data.get("street"),
                latitude = data.get("latitude"),
                longitude = data.get("longitude")
            ),
            locations = [
                justJoinItDTO.Location(
                    city = location.get("city"),
                    slug = location.get("slug"),
                    street = location.get("street"),
                    latitude = location.get("latitude"),
                    longitude = location.get("longitude")
                ) for location in data.get("multilocation")
            ],
            experienceLevel = data.get("experienceLevel")
        )

print(DTOParser.parse(
    {  "slug": "cloudferro-s-a-analityk-systemowy",
            "title": "Analityk Systemowy",
            "requiredSkills": [
                "SQL",
                "UML",
                "REST API",
                "CI/CD",
                "Microservices"
            ],
            "niceToHaveSkills": None,
            "workplaceType": "hybrid",
            "workingTime": "full_time",
            "experienceLevel": "mid",
            "employmentTypes": [
                {
                    "to": 14000,
                    "from": 11000,
                    "type": "permanent",
                    "to_chf": 3124.45,
                    "to_eur": 3252.62,
                    "to_gbp": 2779.77,
                    "to_pln": "14000",
                    "to_usd": 3562.09,
                    "currency": "pln",
                    "from_chf": 2454.925,
                    "from_eur": 2555.63,
                    "from_gbp": 2184.105,
                    "from_pln": "11000",
                    "from_usd": 2798.785
                },
                {
                    "to": 14000,
                    "from": 11000,
                    "type": "b2b",
                    "to_chf": 3124.45,
                    "to_eur": 3252.62,
                    "to_gbp": 2779.77,
                    "to_pln": "14000",
                    "to_usd": 3562.09,
                    "currency": "pln",
                    "from_chf": 2454.925,
                    "from_eur": 2555.63,
                    "from_gbp": 2184.105,
                    "from_pln": "11000",
                    "from_usd": 2798.785
                }
            ],
            "categoryId": 17,
            "multilocation": [
                {
                    "city": "Warszawa",
                    "slug": "cloudferro-s-a-analityk-systemowy",
                    "street": "Fabryczna 5",
                    "latitude": 52.2245849,
                    "longitude": 21.0410065
                },
                {
                    "city": "Kraków",
                    "slug": "cloudferro-s-a-analityk-systemowy-krakow",
                    "street": "-",
                    "latitude": 50.0646501,
                    "longitude": 19.9449799
                },
                {
                    "city": "Wrocław",
                    "slug": "cloudferro-s-a-analityk-systemowy-wroclaw",
                    "street": "-",
                    "latitude": 51.1078852,
                    "longitude": 17.0385376
                },
                {
                    "city": "Gdańsk",
                    "slug": "cloudferro-s-a-analityk-systemowy-gdansk",
                    "street": "-",
                    "latitude": 54.3520252,
                    "longitude": 18.6466384
                },
                {
                    "city": "Poznań",
                    "slug": "cloudferro-s-a-analityk-systemowy-poznan",
                    "street": "-",
                    "latitude": 52.406374,
                    "longitude": 16.9251681
                },
                {
                    "city": "Katowice",
                    "slug": "cloudferro-s-a-analityk-systemowy-katowice",
                    "street": "-",
                    "latitude": 50.2648919,
                    "longitude": 19.0237815
                }
            ],
            "city": "Warszawa",
            "street": "Fabryczna 5",
            "latitude": "52.2245849",
            "longitude": "21.0410065",
            "companyName": "CloudFerro S.A.",
            "companyLogoThumbUrl": "https://public.justjoin.it/offers/company_logos/thumb_x2/31c78306f402d2eb6d07a5e532991498e053453d.png?1707865477",
            "publishedAt": "2024-03-08T23:00:03.660Z",
            "remoteInterview": True,
            "openToHireUkrainians": True
        }
))