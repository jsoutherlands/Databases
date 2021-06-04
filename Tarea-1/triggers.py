
def triggerCasosComuna(cursor):
	cursor.execute(
		"""
			CREATE OR REPLACE TRIGGER CASOS_COMUNA
		    BEFORE UPDATE ON CASOS_POR_COMUNA
		    FOR EACH ROW
		    DECLARE
		    BEGIN 
		        IF :NEW.CASOS_CONFIRMADOS < 0 THEN
		            :NEW.CASOS_CONFIRMADOS := 0;
		        END IF;
		    END;
		""")

def triggerCasosRegion(cursor):
	cursor.execute(
		"""
		CREATE OR REPLACE TRIGGER CASOS_REGION
		BEFORE UPDATE ON CASOS_POR_REGION
		FOR EACH ROW
		DECLARE
		BEGIN 
			IF :NEW.CASOS_CONFIRMADOS < 0 THEN
				:NEW.CASOS_CONFIRMADOS := 0;
			END IF;
		END;
		""")
