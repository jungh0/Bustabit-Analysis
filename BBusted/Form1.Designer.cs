namespace BBusted
{
    partial class BUSTED
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.Num = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.Num2 = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(6, 20);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(588, 376);
            this.panel1.TabIndex = 0;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.panel1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(600, 402);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "WEB";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.Num2);
            this.groupBox2.Controls.Add(this.button1);
            this.groupBox2.Controls.Add(this.Num);
            this.groupBox2.Location = new System.Drawing.Point(12, 420);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(304, 52);
            this.groupBox2.TabIndex = 2;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "SETTING";
            // 
            // Num
            // 
            this.Num.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.Num.Location = new System.Drawing.Point(6, 20);
            this.Num.Name = "Num";
            this.Num.Size = new System.Drawing.Size(100, 21);
            this.Num.TabIndex = 0;
            this.Num.Text = "2547470";
            this.Num.TextChanged += new System.EventHandler(this.Num_TextChanged);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(218, 20);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "Start";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Num2
            // 
            this.Num2.Location = new System.Drawing.Point(112, 20);
            this.Num2.Name = "Num2";
            this.Num2.Size = new System.Drawing.Size(100, 21);
            this.Num2.TabIndex = 2;
            this.Num2.Text = "2547468";
            this.Num2.TextChanged += new System.EventHandler(this.Num2_TextChanged);
            // 
            // BUSTED
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(625, 483);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "BUSTED";
            this.Text = "BUSTED";
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox Num;
        private System.Windows.Forms.TextBox Num2;
    }
}

