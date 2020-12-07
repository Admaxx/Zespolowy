using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Http;

namespace ProsteApi.Controllers
{
    public class MlController : ApiController
    {
        Models.SimpleCalc calc = new Models.SimpleCalc();

        [Route("api/mno/{first}_{second}")]
        public int Get(int first, int second)
        {



            MySqlConnection conn = WebApiConfig.Conn();

            conn.Open();

            MySqlDataAdapter Inserter = new MySqlDataAdapter();
            string query = "insert into wyniki (Wynik, Skl1, Dzialanie, Skl2) values " +
                "(" + calc.Mul(first, second) + "," + first + ',' + "'*'" + ',' + second + ")";


            //MySqlDataReader reader = cmd.ExecuteReader();

            Inserter.InsertCommand = new MySqlCommand(query, conn);

            Inserter.InsertCommand.ExecuteNonQuery();

            return calc.Mul(first, second);
        }
    }
}