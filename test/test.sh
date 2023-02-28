TESTES="test"
DIR_OF_SCRIPTS="test"
VERBOSE="false"

while [ $# -gt 0 ]; do
  key="$1"
  value="$2"

  case $key in
  --dir)
    DIR=$value
    shift 2
    ;;
  --arq)
    ARQ=$value
    shift 2
    ;;
  --test_dir)
    TESTES=$value
    shift 2
    ;;
  --test)
    TESTE=$value
    TIPO_DE_TESTE="unique"
    shift 2
    ;;
  --verbose)
    VERBOSE="true"
    shift 1
    ;;
  *)
    echo "Chave inválida: $key"
    exit 1
    ;;
  esac
done

EXE=$DIR/main.exe

g++ $DIR/$ARQ -Wall -o $EXE

if [ "$TIPO_DE_TESTE" = "unique" ]; then
  echo "python $DIR_OF_SCRIPTS/unique_test.py $TESTE $EXE $TESTES"
  python $DIR_OF_SCRIPTS/unique_test.py $TESTE $EXE $TESTES
else
  echo "python $DIR_OF_SCRIPTS/test.py $TESTES $EXE $VERBOSE"
  python $DIR_OF_SCRIPTS/test.py $TESTES $EXE $VERBOSE
fi
