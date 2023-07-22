from pymodbus.client import ModbusTcpClient
# -*- coding: utf_8 -*-
import sys
# import logging
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp


# pymodbus_client worked with modbus slave
# error when connect to pymodebusslave
def test_pymodbus_client():
    client = ModbusTcpClient('127.0.0.1', port=5020)
    client.connect()
    client.write_coil(2, True)
    result = client.read_coils(2, 1)
    print(result.bits)
    print(result.bits[0])
    client.close()


# worked with pymodbusslave and modbus slave tool
def test_modbus_tk():
    try:
        # 连接MODBUS TCP从机
        master = modbus_tcp.TcpMaster(host="127.0.0.1", port=5020)
        master.set_timeout(5.0)
        # logger.info("connected")
        print('connected')
        # 读保持寄存器
        #data = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 3)
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 3))
        # logger.info(type(data))
        #return data
        # 读输入寄存器
        # logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 0, 16))
        # 读线圈寄存器
        # logger.info(master.execute(1, cst.READ_COILS, 0, 16))
        data = master.execute(1, cst.READ_COILS, 1, 1)
        return data
        # 读离散输入寄存器
        # logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 16))
        # 单个读写寄存器操作
        # 写寄存器地址为0的保持寄存器
        # logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 0, output_value=21))
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1))
        # 写寄存器地址为0的线圈寄存器，写入内容为0（位操作）
        # logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 0, output_value=0))
        # logger.info(master.execute(1, cst.READ_COILS, 0, 1))
        # 多个寄存器读写操作
        # 写寄存器起始地址为0的保持寄存器，操作寄存器个数为4
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[20,21,22,23]))
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4))
        # 写寄存器起始地址为0的线圈寄存器
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0,0,0,0]))
        # logger.info(master.execute(1, cst.READ_COILS, 0, 4))
    except:  # modbus_tk.modbus.ModbusError as e:
        print('MB error')
        # logger.error("%s- Code=%d" % (e, e.get_exception_code()))


if __name__ == "__main__":
    data = test_modbus_tk()
    print(data)
    print(data[0])
