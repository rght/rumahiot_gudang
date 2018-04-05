# Consist of class and methods for accessing surat endpoint
import requests
from rumahiot_gudang.settings import RUMAHIOT_SURAT_API_KEY, RUMAHIOT_SURAT_SEND_DEVICE_NOTIFICATION_ENDPOINT, SEND_ANDROID_NOTIFICATION_ENDPOINT

class GudangSuratModule:


    # Send device notification data to specified email
    # This method will work as a worker, the request will be sent by another thread
    # Input parameter :
    # email(string), device_name(string), user_sensor_name(string)
    # threshold_value(string), latest_value(string), time_reached(string, unix timestamp)
    # threshold_direction((string, 1 or -1), unit_symbol(string)
    # notification_type(string, 0 or 1)
    # output_parameter = requests response object
    def send_device_notification_email_worker(self, user_uuid, user_sensor_uuid,  device_uuid,  email, device_name, user_sensor_name,
                                       threshold_value, latest_value, time_reached,
                                       threshold_direction, unit_symbol,
                                       notification_type):
        header = {
            'Authorization': 'Bearer {}'.format(RUMAHIOT_SURAT_API_KEY)
        }
        payload = {
            'email': email,
            'device_name': device_name,
            'user_sensor_name': user_sensor_name,
            'threshold_value': threshold_value,
            'latest_value': latest_value,
            'time_reached': time_reached,
            'threshold_direction': threshold_direction,
            'unit_symbol': unit_symbol,
            'notification_type': notification_type
        }

        response = requests.post(url=RUMAHIOT_SURAT_SEND_DEVICE_NOTIFICATION_ENDPOINT, headers=header, data=payload)
        return response

    # Send android device notification
    # This endpoint wasn't managed by Rumah IoT
    # Intended to be used on different project, you can remove this part
    # And remove the call in the view
    # Input parameter :
    # - user_uuid (string)
    # - device_uuid(string)
    # - user_sensor_name(string)
    # - user_sensor_uuid(string)
    # - status(string)
    def send_device_android_notification_worker(self, user_uuid, device_uuid, user_sensor_name, user_sensor_uuid, status):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            'user_uuid': user_uuid,
            'device_uuid': device_uuid,
            'user_sensor_name': user_sensor_name,
            'user_sensor_uuid': user_sensor_uuid,
            'status': status
        }
        response = requests.post(url=SEND_ANDROID_NOTIFICATION_ENDPOINT,data=payload, headers=header)
        return response

