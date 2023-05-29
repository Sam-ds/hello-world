import qrcode
import pandas as pd

shipping_items_df = pd.read_csv('shipping_items.csv')
outline_trip_info = shipping_items_df[["vehicle_no", "TripId", "Destination_Location", "Material Shipped"]]
print(outline_trip_info)
fill_color_map = {"perishable_items": "green", "electronics": "white", "clothing": "cyan"}
for index, row in outline_trip_info.iterrows():
    if index < 100:
        vehicle_no = row['vehicle_no']
        trip_id = str(row['TripId']).replace("/","-")
        destination_Location = row['Destination_Location']
        material_Shipped = row['Material Shipped']
        qr_unique_file_name = vehicle_no + "--" + trip_id
        # creating a QRCode object
        obj_qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        obj_qr.add_data(qr_unique_file_name + "--" + destination_Location )
        # using the make() function
        obj_qr.make(fit=True)
        # using the make_image() function
        qr_img = obj_qr.make_image(fill_color=fill_color_map[material_Shipped], back_color="black")
        # saving the QR code image
        qr_img.save(qr_unique_file_name + ".jpg")
