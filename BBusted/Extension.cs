using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BBusted
{
    static class Extension
    {
        //스플릿
        public static string[] Split(this string self, string slash)
        {
            return self.Split(new string[] { slash }, StringSplitOptions.None);
        }

        //딜레이
        public static DateTime Delay(int MS)
        {
            DateTime ThisMoment = DateTime.Now;
            TimeSpan duration = new TimeSpan(0, 0, 0, 0, MS);
            DateTime AfterWards = ThisMoment.Add(duration);

            while (AfterWards >= ThisMoment)
            {
                Application.DoEvents();
                ThisMoment = DateTime.Now;
            }

            return DateTime.Now;
        }

        //텍스트박스 수정하면 숫자인지 판단하고 맞으면 저장
        private static Dictionary<string, int> numberValues = new Dictionary<string, int>();
        public static void setBoxNum(ref TextBox textbox, ref int tmp)
        {
            try
            {
                var num = int.Parse(textbox.Text);
                if (!numberValues.ContainsKey(textbox.Name))
                {
                    numberValues.Add(textbox.Name, num);
                }
                else
                {
                    numberValues[textbox.Name] = num;
                }
                tmp = num;
            }
            catch
            {
                textbox.Text = $"{numberValues[textbox.Name]}";
            }
        }

        //메인 파싱 함수
        public static void parseData(ref string result, int gameNum, string shtml)
        {
            //게임번호
            var newLine = gameNum.ToString() + ",";

            //배수
            var busted_at = shtml
                .Split("<span class=\"key-muted\">Busted at: </span>")[1]
                .Split("<span class=\"bold\"> ")[1]
                .Split("</span>")[0]
                .Replace("x", "");
            newLine += busted_at + ",";

            //스플릿 준비
            var data = shtml
               .Split("<tbody>")[1]
               .Split("</tbody>>")[0];

            //베팅금액
            var betResult = 0;
            var betArr = data.Split("</a></td><td>");

            foreach (var tmp in betArr)
            {
                try
                {
                    var tmpN = tmp.Split("</td>")[0].Replace(",", "");
                    betResult += int.Parse(tmpN);
                }
                catch { }
            }
            newLine += betResult.ToString() + ",";

            //수익금액
            var profitResult = 0;

            //+부분
            var profitArr = data.Split("x</td><td>");
            foreach (var tmp in profitArr)
            {
                try
                {
                    var tmpN = tmp.Split("</td>")[0].Replace(",", "");
                    profitResult += int.Parse(tmpN);
                }
                catch { }
            }

            //-부분
            profitArr = data.Split("-</td><td>");
            foreach (var tmp in profitArr)
            {
                try
                {
                    var tmpN = tmp.Split("</td>")[0].Replace(",", "");
                    profitResult += int.Parse(tmpN);
                }
                catch { }
            }

            //수익저장
            newLine += profitResult.ToString();


            result += newLine + "\n";
        }

    }
}
