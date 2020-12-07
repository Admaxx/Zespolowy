using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Http;

namespace ProsteApi.Controllers
{
    public class ResultsController : ApiController
    {
       [Route("api/results")]
       public string Get()
        {
            MySqlConnection conn = WebApiConfig.Conn();

            conn.Open();

            string query = "Select * from wyniki";


            MySqlCommand cmd = new MySqlCommand(query, conn);
            MySqlDataReader reader = cmd.ExecuteReader();

            string results = "";
            while (reader.Read())
                results += Environment.NewLine+" ID: "+ reader["id"].ToString()+ " Wynik: " 
                    + reader["Wynik"].ToString() +" Data: "
                    + reader["Data"].ToString();

            return results;



        }
        
    }
}