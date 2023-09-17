from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class CurrentAPIView(APIView):
    def get(self, request):
        other_response = \
            (requests.get("https://www.cbr-xml-daily.ru/latest.js")
            .json()["rates"])

        response = request.GET
        try:
            if response.get("from") != "RUB":
                response_from = other_response[response.get("from")]
            response_to = other_response[response.get("to")]
            response_value = int(response.get("value"))
            if response.get("to") == "RUB":
                return Response({"result": round(
                                (1 / response_from)
                                * response_value, 2)
                                 })
            elif response.get("from") == "RUB":
                return Response({"result": round(
                                response_to
                                * response_value, 2)
                                 })
            else:
                return Response({"result": round(
                                (1 / response_from) /
                                (1 / response_to)
                                * response_value, 2)
                                 })
        except KeyError:
            return Response({"result": "К сожалению такую валюту конвертировать не можем"})
        except:
            return Response({"result": "Неверный ввод"})

