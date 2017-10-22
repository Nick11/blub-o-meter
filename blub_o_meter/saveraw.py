import LSM6DS3
import time

ENDIANNESS = 'big'

sensor = LSM6DS3.LSM6DS3()
with open('rawdata-' + time.strftime('%Y%m%d%H%M%S'), 'wb') as f:
    # Write header
    f.write((0xb100bb100b000000).to_bytes(8, ENDIANNESS))
    start_timestamp = time.time()
    f.write(int(start_timestamp * 1000).to_bytes(8, ENDIANNESS))

    for val in sensor.accelvalues():
        # Write acceleration values
        for accel_coord in val:
            f.write(accel_coord.to_bytes(2, ENDIANNESS, signed = True))

        timestamp_offset = int(1000 * (time.time() - start_timestamp))

        # Exit on timestamp offset overflow
        if timestamp_offset.bit_length() > 32:
            break

        # Write timestamp offset
        f.write(timestamp_offset.to_bytes(4, ENDIANNESS))
