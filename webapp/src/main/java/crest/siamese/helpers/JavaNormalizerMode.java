package crest.siamese.helpers;

import crest.siamese.settings.NormalizerMode;
import crest.siamese.settings.Settings;

public class JavaNormalizerMode implements NormalizerMode {

	private int word;
	private int keyword;
	private int datatype;
	private int javaClass;
	private int javaPackage;
	private int operator;
	private int string;
	private int value;
	private int escape;

	public JavaNormalizerMode() {
		super();
		word = Settings.Normalize.WORD_NORM_OFF;
		keyword = Settings.Normalize.KEYWORD_NORM_OFF;
		javaClass = Settings.Normalize.JAVACLASS_NORM_OFF;
		javaPackage = Settings.Normalize.JAVAPACKAGE_NORM_OFF;
		operator = Settings.Normalize.OPERATOR_NORM_OFF;
		string = Settings.Normalize.STRING_NORM_OFF;
		value = Settings.Normalize.STRING_NORM_OFF;
		escape = Settings.Normalize.ESCAPE_OFF;
		datatype = Settings.Normalize.DATATYPE_NORM_OFF;
	}

	public JavaNormalizerMode(int word,	int keyword, int datatype,int javaClass,int javaPackage,int string,int value,int escape,int operator) {
		this.word = word;
		this.keyword = keyword;
		this.javaClass = javaClass;
		this.javaPackage = javaPackage;
		this.string = string;
		this.value = value;
		this.escape = escape;
		this.datatype = datatype;
		this.operator = operator;
	}

	@Override
	public void configure(char[] normOptions) {
		for (char c : normOptions) {
			// setting all normalisation options: w, d, j, p, k, v, s
			switch (Character.toLowerCase(c)) {
				case 'w':
					word = Settings.Normalize.WORD_NORM_ON;
					break;
				case 'd':
					datatype = Settings.Normalize.DATATYPE_NORM_ON;
					break;
				case 'j':
					javaClass = Settings.Normalize.JAVACLASS_NORM_ON;
					break;
				case 'p':
					javaPackage = Settings.Normalize.JAVAPACKAGE_NORM_ON;
					break;
				case 'k':
					keyword = Settings.Normalize.KEYWORD_NORM_ON;
					break;
				case 'r':
					keyword = Settings.Normalize.KEYWORD_REMOVE;
					break;
				case 'v':
					value = Settings.Normalize.VALUE_NORM_ON;
					break;
				case 's':
					string = Settings.Normalize.STRING_NORM_ON;
					break;
				case 'o':
					operator = Settings.Normalize.OPERATOR_NORM_ON;
					break;
				case 'x':
					word = Settings.Normalize.WORD_NORM_OFF;
					datatype = Settings.Normalize.DATATYPE_NORM_OFF;
					javaClass = Settings.Normalize.JAVACLASS_NORM_OFF;
					javaPackage = Settings.Normalize.JAVAPACKAGE_NORM_OFF;
					keyword = Settings.Normalize.KEYWORD_NORM_OFF;
					value = Settings.Normalize.VALUE_NORM_OFF;
					string = Settings.Normalize.STRING_NORM_OFF;
					operator = Settings.Normalize.OPERATOR_NORM_OFF;
					break;
				case 'e':
					escape = Settings.Normalize.ESCAPE_ON;
					break;
				default:
					word = Settings.Normalize.WORD_NORM_OFF;
					datatype = Settings.Normalize.DATATYPE_NORM_OFF;
					javaClass = Settings.Normalize.JAVACLASS_NORM_OFF;
					javaPackage = Settings.Normalize.JAVAPACKAGE_NORM_OFF;
					keyword = Settings.Normalize.KEYWORD_NORM_OFF;
					value = Settings.Normalize.VALUE_NORM_OFF;
					string = Settings.Normalize.STRING_NORM_OFF;
					operator = Settings.Normalize.OPERATOR_NORM_OFF;
					break;
			}
		}
	}

	@Override
	public void reset() {
		word = Settings.Normalize.WORD_NORM_OFF;
		keyword = Settings.Normalize.KEYWORD_NORM_OFF;
		javaClass = Settings.Normalize.JAVACLASS_NORM_OFF;
		javaPackage = Settings.Normalize.JAVAPACKAGE_NORM_OFF;
		string = Settings.Normalize.STRING_NORM_OFF;
		value = Settings.Normalize.STRING_NORM_OFF;
		escape = Settings.Normalize.ESCAPE_OFF;
		datatype = Settings.Normalize.DATATYPE_NORM_OFF;
		operator = Settings.Normalize.OPERATOR_NORM_OFF;
	}

	public int getWord() {
		return word;
	}

	public void setWord(int word) {
		this.word = word;
	}

	public int getKeyword() {
		return keyword;
	}

	public void setKeyword(int keyword) {
		this.keyword = keyword;
	}

	public int getDatatype() {
		return datatype;
	}

	public void setDatatype(int datatype) {
		this.datatype = datatype;
	}

	public int getJavaClass() {
		return javaClass;
	}

	public void setJavaClass(int javaClass) {
		this.javaClass = javaClass;
	}

	public int getJavaPackage() {
		return javaPackage;
	}

	public void setJavaPackage(int javaPackage) {
		this.javaPackage = javaPackage;
	}

	public int getOperator() {
		return operator;
	}

	public void setOperator(int operator) {
		this.operator = operator;
	}

	public int getString() {
		return string;
	}

	public void setString(int string) {
		this.string = string;
	}

	public int getValue() {
		return value;
	}

	public void setValue(int value) {
		this.value = value;
	}

	public int getEscape() {
		return escape;
	}

	public void setEscape(int escape) {
		this.escape = escape;
	}
}
