from ast import Return
import copy
from pandas import read_sql

class ListenMsg:
    def __init__(self, koneksi_db):
        self.koneksi = koneksi_db
        try:
            self.cursor = self.koneksi.cursor()
        except:
            pass

    async def handler(self, method: str, request_json_data: dict):
        response_json_data = copy.deepcopy(request_json_data)

        response_json_data['response'] = '999'
        response_json_data['responseMessage'] = "General Error"

        if method == 'INFO-REKENING':
            response_json_data = await self.info_rekening(request_json_data)
        elif method == 'INFO-SALDO':
            response_json_data = await self.info_rekening(request_json_data)

        return response_json_data

    async def info_rekening(self, request_json_data: dict):
        #olah data info rekening
        
        response_json_data = {
            "response": "999",
            "responseMessage": "General Error",
        }

        ls_no_rekening = request_json_data.get('nokontrak')

        query = "SELECT a.*, TOFLMB.nokontrak, TOFLMB.nama, TOFLMB.acpok, TOFLMB.mgnawal, TOFLMB.mdlawal, TOFLMB.noakad, TOFLMB.tgleff, TOFLMB.tglakad FROM SETUPLOAN a INNER JOIN TOFLMB ON a.kdprd=TOFLMB.kdprd WHERE TOFLMB.nokontrak = ?"
        qparms = [ls_no_rekening]

        dataFrame = read_sql(query, self.koneksi, params=qparms)

        print(dataFrame)
        
        
        if ls_no_rekening == dataFrame['nokontrak'][0]:
            response_json_data['response'] = '200'
            response_json_data['responseMessage'] = 'SUCCESS'
            response_json_data['ContractNumber'] = dataFrame['nokontrak'][0]
            response_json_data['CodeProduct'] = dataFrame['kdprd'][0]
            response_json_data['AdditionalInfo'] = dataFrame['ket'][0] 
            response_json_data['Name'] = dataFrame['nama'][0]
            response_json_data['AccountsPayments'] = dataFrame['acpok'][0]
            response_json_data['InitialMargin'] = dataFrame['mgnawal'][0]
            response_json_data['InitialModal'] = dataFrame['mdlawal'][0]
            response_json_data['AkadNumber'] = dataFrame['noakad'][0]
            response_json_data['EffectiveDate'] = dataFrame['tgleff'][0]
            response_json_data['ContractDate'] = dataFrame['tglakad'][0]
            response_json_data["HashValue"] = (str(hash(dataFrame['nokontrak'][0]))) 
            if (str(hash(dataFrame['nokontrak'][0]))) == (str(hash(dataFrame['nokontrak'][0]))):
                 response_json_data ['Status']=('Validate')
            else:
                response_json_data ['Status']=('Not Validate')

              
        else:
            response_json_data['response'] = '101'
            response_json_data['responseMessage'] = 'INVALID ACCOUNT NO'                
    
        return response_json_data


   

    
