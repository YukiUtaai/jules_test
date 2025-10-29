import argparse
import qrcode

def generate_qr_code(data, filename):
    """
    指定されたデータからQRコードを生成し、ファイルに保存する

    :param data: QRコードにする文字列
    :param filename: 保存する画像ファイル名
    """
    img = qrcode.make(data)
    img.save(filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a QR code from a given string.")
    parser.add_argument("data", help="The data to encode in the QR code.")
    parser.add_argument("-o", "--output", help="The output filename.", default="qrcode.png")
    args = parser.parse_args()

    generate_qr_code(args.data, args.output)
    print(f"QR code saved to {args.output}")
