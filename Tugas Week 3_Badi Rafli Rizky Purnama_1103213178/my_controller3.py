from controller import Robot

# Buat objek robot
robot = Robot()

# Tentukan waktu simulasi
waktu_simulasi = int(robot.getBasicTimeStep())

# Aktifkan sensor proximity depan (sensor 0 dan sensor 7)
sensor_depan_kiri = robot.getDevice('ps0')
sensor_depan_kanan = robot.getDevice('ps7')
sensor_depan_kiri.enable(waktu_simulasi)
sensor_depan_kanan.enable(waktu_simulasi)

# Aktifkan motor kiri dan kanan
motor_kiri = robot.getDevice('left wheel motor')
motor_kanan = robot.getDevice('right wheel motor')
motor_kiri.setPosition(float('inf'))  # Mode kecepatan
motor_kanan.setPosition(float('inf'))

# Fungsi untuk menggerakkan robot maju
def jalan_maju(kecepatan):
    motor_kiri.setVelocity(kecepatan)
    motor_kanan.setVelocity(kecepatan)

# Fungsi untuk menghentikan robot
def berhenti():
    motor_kiri.setVelocity(0)
    motor_kanan.setVelocity(0)

# Program utama berjalan terus selama simulasi aktif
while robot.step(waktu_simulasi) != -1:
    # Baca nilai sensor depan
    ada_objek_depan = sensor_depan_kiri.getValue() > 80 or sensor_depan_kanan.getValue() > 80
    
    # Jika ada objek di depan, berhenti
    if ada_objek_depan:
        berhenti()
    else:
        jalan_maju(3)  # Kalau tidak ada objek, jalan maju dengan kecepatan 3
