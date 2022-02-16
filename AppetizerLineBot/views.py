from django.shortcuts import render, resolve_url
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser, webhook
import linebot
from linebot import exceptions
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from .scraper import Appetizer, Avgle, Netflav, Av01

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
            
        for event in events:
            if isinstance(event, MessageEvent):
                result1 = Avgle(event.message.text) #番號存入class
                result2 = Netflav(event.message.text)
                result3 = Av01(event.message.text)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=result1.scrape()+result2.scrape()+result3.scrape())
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
