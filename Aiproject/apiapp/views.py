from django.shortcuts import render



import requests, os, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}


def index(request):
    return render(request, "index.html")




@csrf_exempt
def ask_ai(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("question", "")

        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": user_input})

            # Check if we got content
            if response.status_code != 200:
                return JsonResponse({"error": f"Hugging Face API error: {response.status_code}"})

            try:
                result = response.json()
            except json.JSONDecodeError:
                return JsonResponse({"error": "Empty or invalid response from Hugging Face"})

            if isinstance(result, list) and "generated_text" in result[0]:
                answer = result[0]["generated_text"]
            else:
                answer = str(result)

            return JsonResponse({"answer": answer})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)