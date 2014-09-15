#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
 
class DataBase:
    
    crear_tablas = '''CREATE TABLE IF NOT EXISTS Turnos(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	nombre_cliente VARCHAR(30) NOT NULL,
	fecha_hora VARCHAR(20) NOT NULL,
	fecha_hora_reserva TIMESTAMP NOT NULL,
	cant_horas INTEGER NOT NULL,
	tipo_cancha VARCHAR(20) NOT NULL
        )'''
    
    def __init__(self):
        self.conn = sqlite3.connect('ElClub')
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.crear_tablas)
    
    def __exit__(self):
        self.close()
    
    def open(self):
        """Abrir conexión y establecer un cursor"""
        self.conn = sqlite3.connect('ElClub')
        self.cursor = self.conn.cursor()
    
    def agregar_turno(self, nombre_cliente, fecha_hora, cant_horas, tipo_cancha):
	"""Inserta los datos en la base de datos """
	params = (nombre_cliente, fecha_hora, cant_horas, tipo_cancha)
	self.cursor.execute("INSERT INTO Turnos(nombre_cliente, fecha_hora_reserva, fecha_hora, cant_horas, tipo_cancha) VALUES(?, datetime('now', 'localtime'), ?, ?, ?)", params)
    
    def mostrar_turnos(self, fecha_hora, tipo_cancha):
        """Muestra todos los turnos en la fecha y hora"""
        q = self.cursor.execute("SELECT nombre_cliente, cant_horas, fecha_hora_reserva FROM Turnos WHERE fecha_hora="+fecha_hora+"AND tipo_cancha="+tipo_cancha)
        return q.fetchall()
    
    def get_all(self):
        """Retorna las filas"""
        q = self.cursor.execute("SELECT * FROM Turnos")
        algo = q.fetchall()
        print algo
    
    def commit(self):
        """Guardar cambios"""
        self.conn.commit()
    
    def close(self):
        self.cursor.close()
        self.conn.close()